import json 


class BaseProfile(object):
    
    def __init__(self, model_name) -> None:
        self.model_name = model_name
        self.temperature = 0.7
        self.streaming = False
        self.__model_kwargs = []

    def __call__(self, max_tokens=128, seed=None):
        # model type-specific (i.e., chat, non-chat) model_kwargs may be added later, 
        # should be added to self.__model_kwargs key list

        # any other params should be added to the config: 
        config = {k: v for k, v in self.__dict__.items() if not k.startswith('_')}
        # add max_tokens at call-time
        config.update({'max_tokens': max_tokens})

        # model_kwargs are separately treated
        model_kwargs = {key: config.pop(key) for key in self.__model_kwargs if key in config}
        # currently, seed only model_kwargs
        if seed: model_kwargs.update({'seed': seed})
        
        config.update({'model_kwargs': model_kwargs})
        return config

    def to_json(self):
        raise NotImplementedError('Implement this function for sub-classes!')
    
    def to_file(self, filename):
        """
        Save the class instance to a file in JSON format.
        """
        with open(filename, 'w') as f:
            json_str = self.to_json()
            f.write(json_str)
    
    @classmethod
    def from_json(cls, json_str):
        raise NotImplementedError('Implement this function for sub-classes!')
        
    @classmethod
    def from_file(cls, filename):
        """
        Save the class instance to a file in JSON format.
        """
        with open(filename, 'r') as f:
            return cls.from_json(json.load(f))
    

class Profile(BaseProfile):
    def __init__(self, model_name='llama2-70b-chat') -> None:
        super().__init__(model_name)
        self.top_p = 1
        self.frequency_penalty = 0
        self.presence_penalty = 0
        self.n = 1
        self.best_of = 1
        self.max_retries = 6
        self.allowed_special = set()
        self.disallowed_special = 'all'
    
    def to_json(self):
        """
        Convert the class instance to a JSON string.
        """
        data = {
            'model_name': self.model_name,
            'temperature': self.temperature,
            'streaming': self.streaming,
            '__model_kwargs': self.__model_kwargs,

            'top_p': self.top_p,
            'frequency_penalty': self.frequency_penalty,
            'presence_penalty': self.presence_penalty,
            'n': self.n,
            'best_of': self.best_of,
            'max_retries': self.max_retries,
            'allowed_special': list(self.allowed_special),
            'disallowed_special': self.disallowed_special,
        }
        return json.dumps(data)
    
    @classmethod
    def from_json(cls, json_str):
        """
        Create a class instance from a JSON string.
        """
        data = json.loads(json_str)
        instance = cls(data.pop('model_name'))
        instance.temperature = data['temperature']
        instance.streaming = data['streaming']
        instance.__model_kwargs = data['__model_kwargs']
        instance.top_p = data['top_p']
        instance.frequency_penalty = data['frequency_penalty']
        instance.presence_penalty = data['presence_penalty']
        instance.n = data['n']
        instance.best_of = data['best_of']
        instance.max_retries = data['max_retries']
        instance.allowed_special = set(data['allowed_special']),
        instance.disallowed_special = data['disallowed_special']
        

class ChatProfile(BaseProfile):
    def __init__(self, model_name='llama2-70b') -> None:
        model_name += '-chat'
        super().__init__(model_name)

    def to_json(self):
        """
        Convert the class instance to a JSON string.
        """
        data = {
            'model_name': self.model_name,
            'temperature': self.temperature,
            'streaming': self.streaming,
            '__model_kwargs': self.__model_kwargs,
        }
        return json.dumps(data)
    
    @classmethod
    def from_json(cls, json_str):
        """
        Create a class instance from a JSON string.
        """
        data = json.loads(json_str)
        instance = cls(data.pop('model_name'))
        instance.temperature = data['temperature']
        instance.streaming = data['streaming']
        instance.__model_kwargs = data['__model_kwargs']
        