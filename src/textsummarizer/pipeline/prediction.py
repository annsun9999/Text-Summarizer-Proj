#Prediction
from textsummarizer.config.configuration import ConfigurationManager
from transformers import AutoTokenizer
from transformers import pipeline 

class PredictionPipeline:
    
   def __init__(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        self.config = model_evaluation_config

   def predict(self,text):
    tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_path)
    gen_kwargs = {"length_penalty": 0.8, "num_beams":8, "max_length": 128}
 ##
    print("Dialogue:")
    print(text)

    pipe = pipeline("summarization", model=self.config.model_path,tokenizer=tokenizer)
    text = pipe(text, **gen_kwargs)[0]["summary_text"]

   

    print("\nModel Summary:")
    print(text)

    return text