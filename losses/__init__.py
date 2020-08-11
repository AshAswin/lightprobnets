from losses import classification_losses
from losses import endpoint_error
from losses import probabilistic_classification_losses
from losses import probabilistic_endpoint_error


ClassificationLoss = classification_losses.ClassificationLoss
DirichletProbOutLoss = probabilistic_classification_losses.DirichletProbOutLoss
MultiScaleEPE = endpoint_error.MultiScaleEPE
MultiScaleLaplacian = probabilistic_endpoint_error.MultiScaleLaplacian
