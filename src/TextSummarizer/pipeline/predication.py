import transformers import AutoTokenzer 
from transformers import pipeline
from TextSummarizer.config.configuration import ConfigManager



class PredicationPipeline:
    def __init__( self ):
        self.config =  ConfigManager().get_model_evaluation_config()


    def predict( self, text ):
        tokenzier = AutoTokenzer.from_pretrained(self.config.tokenizer_path)
        gen_kwargs = { "lengthy_penality" : 0.8 , "max_length" : 128, "num_beams": 8 }
        pipe = pipeline("summarization", tokenizer=tokenzier, model = self.config.model_path )

        print( "Dialogue:")
        print(text)

        output = pipe(text, **gen_kwargs)[0]['summary_text']

        print("\nModel Summary:\n")
        print( output )
        return output



