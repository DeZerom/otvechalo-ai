from deeppavlov import build_model


class ContextQuestionAnswering:

    def __init__(self):
        self.model = build_model(
            config='qa_multisberquad_bert',
            install=True,
            download=True
        )

    def get_answer(self, context: str, query: str) -> str:
        return self.model(context, query)


model = ContextQuestionAnswering()


def get_answer(context: str, query: str) -> str:
    return model.get_answer(context, query)
