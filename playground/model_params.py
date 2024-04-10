from typing import Field, Dict, Any, Optional, Union, Tuple, Literal, AbstractSet, Collection

model_name: str = Field(default="text-davinci-003", alias="model")
"""Model name to use."""

temperature: float = 0.7
"""What sampling temperature to use."""

max_tokens: int = 256
"""The maximum number of tokens to generate in the completion.
-1 returns as many tokens as possible given the prompt and
the models maximal context size."""

top_p: float = 1
"""Total probability mass of tokens to consider at each step."""

frequency_penalty: float = 0
"""Penalizes repeated tokens according to frequency."""

presence_penalty: float = 0
"""Penalizes repeated tokens."""

n: int = 1
"""How many completions to generate for each prompt."""

best_of: int = 1
"""Generates best_of completions server-side and returns the "best"."""

model_kwargs: Dict[str, Any] = Field(default_factory=dict)
"""Holds any model parameters valid for `create` call not explicitly specified."""

openai_api_key: Optional[str] = None

openai_api_base: Optional[str] = None

openai_organization: Optional[str] = None
# to support explicit proxy for OpenAI

openai_proxy: Optional[str] = None

batch_size: int = 20
"""Batch size to use when passing multiple documents to generate."""

request_timeout: Optional[Union[float, Tuple[float, float]]] = None
"""Timeout for requests to OpenAI completion API. Default is 600 seconds."""

logit_bias: Optional[Dict[str, float]] = Field(default_factory=dict)
"""Adjust the probability of specific tokens being generated."""

max_retries: int = 6
"""Maximum number of retries to make when generating."""

streaming: bool = False
"""Whether to stream the results or not."""

allowed_special: Union[Literal["all"], AbstractSet[str]] = set()
"""Set of special tokens that are allowed。"""

disallowed_special: Union[Literal["all"], Collection[str]] = "all"
"""Set of special tokens that are not allowed。"""

tiktoken_model_name: Optional[str] = None
"""The model name to pass to tiktoken when using this class. 
Tiktoken is used to count the number of tokens in documents to constrain 
them to be under a certain limit. By default, when set to None, this will 
be the same as the embedding model name. However, there are some cases 
where you may want to use this Embedding class with a model name not 
supported by tiktoken. This can include when using Azure embeddings or 
when using one of the many model providers that expose an OpenAI-like 
API but with different models. In those cases, in order to avoid erroring 
when tiktoken is called, you can specify a model name to use here."""
