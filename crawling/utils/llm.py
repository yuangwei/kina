from langchain.llms import LLMChain
from langchain.chains import AnalyzeDocumentChain
from langchain.prompts import PromptTemplate
from langchain.text_splitter import CharacterTextSplitter
from langchain.llms import LlamaCpp

prompt_template = """
You are an experienced SaaS product manager. 
Your goal is to analyze the given text and identify potential market needs or opportunities for new SaaS products or features.
Focus on finding patterns, common pain points, or unmet needs expressed in the text.
Output your analysis in the following format:

SaaS Opportunity 1:
Description:
Supporting Evidence:

SaaS Opportunity 2:
Description: 
Supporting Evidence:

...

"""

prompt = PromptTemplate(template=prompt_template, input_variables=["text"])
llm = LlamaCpp(model_path="path/to/llama/model")
chain = AnalyzeDocumentChain(combine_docs_chain=LLMChain(llm=llm, prompt=prompt))
