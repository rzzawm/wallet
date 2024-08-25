from rich.prompt import PromptBase, InvalidResponse, Prompt


class AmountPrompt(PromptBase[float]):
    def process_response(self, value: str) -> float:
        try:
            float_value = float(value)
        except ValueError:
            raise InvalidResponse("Amount should be a number!")
        if float_value <= 0.1:
            raise InvalidResponse("Amount should be greater than 0.1!")
        return float_value


class DescriptionPrompt(PromptBase[str]):
    def process_response(self, value: str) -> str:
        value = value.strip()
        if len(value) > 127:
            raise InvalidResponse(
                "Description length should be less than 127 characters")
        if value and len(value) < 3:
            raise InvalidResponse("Write at least 3 charachters")
        return value
