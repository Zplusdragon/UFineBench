from prettytable import PrettyTable
import torch
import logging
import math
from itertools import accumulate
def mSD_rank(similarity, q_pids, g_pids, max_rank=10):
    similarity = similarity / 2 + 0.5 # Normalize similarity to [0, 1]
    indices = torch.argsort(similarity, dim=1, descending=True)
    pred_labels = g_pids[indices.cpu()]
    matches = pred_labels.eq(q_pids.view(-1, 1))
    all_cmc = matches[:, :max_rank].cumsum(1)
    all_cmc[all_cmc > 1] = 1
    all_cmc = all_cmc.float().mean(0) * 100

    postive_idx = (indices+1)*matches
    postive_idx[postive_idx>=1] = 1
    postive_similarity = similarity*postive_idx

    num_rel = matches.sum(1)
    postive_similarity_sum = postive_similarity.sum(1)
    negative_similarity_sum = similarity.sum(1)-postive_similarity_sum
    postive_similarity_average = postive_similarity_sum/num_rel
    negative_similarity_average = negative_similarity_sum/(similarity.shape[1]-num_rel)
    pn_ratio = (postive_similarity_average / negative_similarity_average).numpy()
    pn_ratio = torch.tensor([1 - math.exp(-x) for x in pn_ratio])
    similarity_cmc = torch.cumsum(similarity, dim=1)
    positive_similarity_cmc = torch.cumsum(postive_similarity, dim=1)
    
    sd_cmc = positive_similarity_cmc/similarity_cmc
    sd_cmc = sd_cmc * matches
    SD = (sd_cmc.sum(1) / num_rel) * pn_ratio
    mSD = SD.mean() * 100

    tmp_cmc = matches.cumsum(1)
    tmp_cmc = [tmp_cmc[:, i] / (i + 1.0) for i in range(tmp_cmc.shape[1])]
    tmp_cmc = torch.stack(tmp_cmc, 1) * matches
    AP = tmp_cmc.sum(1) / num_rel
    mAP = AP.mean() * 100
    return all_cmc, mSD, mAP


class Calculator():
    def __init__(self, img_loader, txt_loader):
        self.img_loader = img_loader  # gallery
        self.txt_loader = txt_loader  # query
        self.logger = logging.getLogger("CFAM.eval")

    def _compute_embedding(self, model):
        model = model.eval()
        device = next(model.parameters()).device
        qids, gids, qfeats, gfeats = [], [], [], []

        # text
        for pid, caption in self.txt_loader:
            caption = caption.to(device)
            with torch.no_grad():
                text_feat = model.encode_text(caption)
            qids.append(pid.view(-1))  # flatten
            qfeats.append(text_feat)
        qids = torch.cat(qids, 0)
        qfeats = torch.cat(qfeats, 0)

        # image
        for pid, img in self.img_loader:
            img = img.to(device)
            with torch.no_grad():
                img_feat = model.encode_image(img)
            gids.append(pid.view(-1))  # flatten
            gfeats.append(img_feat)
        gids = torch.cat(gids, 0)
        gfeats = torch.cat(gfeats, 0)

        return qfeats, gfeats, qids, gids

    def eval(self, model):
        qfeats, gfeats, qids, gids = self._compute_embedding(model)
        qfeats = torch.nn.functional.normalize(qfeats, p=2, dim=1)  # text features
        gfeats = torch.nn.functional.normalize(gfeats, p=2, dim=1)  # image features
        similarity = qfeats @ gfeats.t()

        t2i_cmc, t2i_mSD, t2i_mAP, _ = mSD_rank(similarity=similarity, q_pids=qids, g_pids=gids, max_rank=10, get_mAP=True)
        t2i_cmc, t2i_mSD, t2i_mAP = t2i_cmc.numpy(), t2i_mSD.numpy(), t2i_mAP.numpy()
        table = PrettyTable(["task", "R1", "R5", "R10", "mSD", "mAP"])
        table.add_row(['t2i', t2i_cmc[0], t2i_cmc[4], t2i_cmc[9], t2i_mSD, t2i_mAP])

        table.custom_format["R1"] = lambda f, v: f"{v:.3f}"
        table.custom_format["R5"] = lambda f, v: f"{v:.3f}"
        table.custom_format["R10"] = lambda f, v: f"{v:.3f}"
        table.custom_format["mSD"] = lambda f, v: f"{v:.3f}"
        table.custom_format["mAP"] = lambda f, v: f"{v:.3f}"
        self.logger.info('\n' + str(table))

        return t2i_cmc[0]


#example
qfeats = torch.randn([10,768])
qids = torch.tensor([1,1,3,7,5,6,6,8,8,10])

gfeats = torch.randn([30,768])
gids = torch.tensor([1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10,11,12,13,14,15,16,17,18,19,20])

qfeats = torch.nn.functional.normalize(qfeats, p=2, dim=1)  # text features
gfeats = torch.nn.functional.normalize(gfeats, p=2, dim=1)  # image features
similarity = qfeats @ gfeats.t()
t2i_cmc, t2i_mSD, t2i_mAP = mSD_rank(similarity=similarity, q_pids=qids, g_pids=gids, max_rank=10)
print(t2i_cmc)
print(t2i_mSD)
print(t2i_mAP)




