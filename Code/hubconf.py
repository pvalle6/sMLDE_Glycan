dependencies = ['torch']
import esm  

# resnet18 is the name of entrypoint
def entry():
    checkpoint = "/ddnA/project/jjung1/pvalle6/checkpoints/esm1b_t33_650M_UR50S.pt"
    state_dict = torch.load(checkpoint)
    model.load_state_dict(state_dict)
    return model
