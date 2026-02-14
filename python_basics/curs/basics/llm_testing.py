import json
import os.path

from gpt4all import GPT4All


class LLM:
    MODELS = (
        'Llama-3.2-1B-Instruct-Q4_0.gguf',
        'qwen2.5-coder-7b-instruct-q4_0.gguf',
        'Meta-Llama-3-8B-Instruct.Q4_0.gguf',
        'DeepSeek-R1-Distill-Qwen-7B-Q4_0.gguf',
        'DeepSeek-R1-Distill-Qwen-14B-Q4_0.gguf',
        'DeepSeek-R1-Distill-Llama-8B-Q4_0.gguf',
        'DeepSeek-R1-Distill-Qwen-1.5B-Q4_0.gguf',
        'Llama-3.2-3B-Instruct-Q4_0.gguf',
        'Llama-3.2-1B-Instruct-Q4_0.gguf',
        'mistral-7b-instruct-v0.1.Q4_0.gguf',
        'Meta-Llama-3.1-8B-Instruct-128k-Q4_0.gguf',
        'mistral-7b-openorca.gguf2.Q4_0.gguf',
        'gpt4all-falcon-newbpe-q4_0.gguf',
        'orca-2-7b.Q4_0.gguf',
        'orca-2-13b.Q4_0.gguf',
        'wizardlm-13b-v1.2.Q4_0.gguf',
        'ghost-7b-v0.9.1-Q4_0.gguf',
        'nous-hermes-llama2-13b.Q4_0.gguf',
        'gpt4all-13b-snoozy-q4_0.gguf',
        'mpt-7b-chat-newbpe-q4_0.gguf',
        'mpt-7b-chat.gguf4.Q4_0.gguf',
        'Phi-3-mini-4k-instruct.Q4_0.gguf',
        'orca-mini-3b-gguf2-q4_0.gguf',
        'replit-code-v1_5-3b-newbpe-q4_0.gguf',
        'starcoder-newbpe-q4_0.gguf',
        'rift-coder-v0-7b-q4_0.gguf',
        'all-MiniLM-L6-v2-f16.gguf',
        'em_german_mistral_v01.Q4_0.gguf',
        'nomic-embed-text-v1.f16.gguf',
        'nomic-embed-text-v1.5.f16.gguf',
        'qwen2-1_5b-instruct-q4_0.gguf',
    )

    MENU = """
        Main menu:
        1. Start chat
        2. Change model
        3.Exit app
        """

    def __init__(self):
        self.load()
        self.__model = GPT4All(LLM.MODELS[self.__mod_index])

    def save(self):
        with open("model_index.json", "w") as f:
            json.dump(self.__mod_index, f)

    def load(self):
        if os.path.exists("model_index.json"):
            with open("model_index.json", "r") as f:
                self.__mod_index = json.load(f)
        else:
            self.__mod_index = 0
            self.save()

    def chat(self):
        prompt = input("(q to quit) >")
        while prompt != 'q':
            print(self.__model.generate(prompt, max_tokens=4096))
            prompt = input("(q to quit) >")

    def change_model(self):
        for i, model in enumerate(LLM.MODELS):
            print(f'{i + 1}. {model}')
        index_input = int(input('Select a model: ')) - 1
        self.__mod_index=index_input
        self.__model = GPT4All(LLM.MODELS[index_input])
        print(f'Changed model to {LLM.MODELS[index_input]}')
        self.save()

    def chat_menu(self):
        print(LLM.MENU)

        selection_input = int(input("Select an option: "))

        while selection_input < 3:
            match selection_input:
                case 1:
                    self.chat()
                case 2:
                    self.change_model()
                case _:
                    pass
            print(LLM.MENU)
            selection_input = int(input("Select an option: "))


def main():
    # model = GPT4All(MODELS[0])  # CPU, adica procesor
    # model = GPT4All(MODELS[0], device='gpu')  # GPU, adica placa video
    # response = model.generate('Tell me a joke', max_tokens=4096)
    # print(response)
    #
    llm = LLM()
    # chat_input = input("Ask a question: ")
    # llm.chat(chat_input)
    llm.chat_menu()


if __name__ == '__main__':
    main()
