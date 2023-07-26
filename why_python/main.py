from model_a import ModelA


model = ModelA.from_dict(
    {
        "a": {
            "a": {},
            "b": {},
        },
        "b": {
            "a": {},
        },
    }
)
print(model)
