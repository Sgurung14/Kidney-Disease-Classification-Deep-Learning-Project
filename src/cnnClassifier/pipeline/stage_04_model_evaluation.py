from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.model_evaluation_mlflow import Evaluation
from cnnClassifier import logger


STAGE_NAME = "Model Evaluation Stage"

class EvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_evaluation_config()
        model_evaluation = Evaluation(config=model_evaluation_config)
        model_evaluation.evaluation()
        model_evaluation.log_into_mlflow()

if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = EvaluationPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
