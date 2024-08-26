from rich.prompt import PromptBase, InvalidResponse, Prompt, Confirm


class AmountPrompt(PromptBase[float]):
    def process_response(self, value: str) -> float:
        try:
            float_value = float(value)
        except ValueError:
            raise InvalidResponse("[yellow]Amount should be a number![/]")
        if float_value <= 0.1:
            raise InvalidResponse(
                "[yellow]Amount should be greater than 0.1![/]")
        return float_value


class DescriptionPrompt(PromptBase[str]):
    def process_response(self, value: str) -> str:
        value = value.strip()
        if len(value) > 127:
            raise InvalidResponse(
                "[yellow]Description length should be less than 127 characters[/]")
        if value and len(value) < 3:
            raise InvalidResponse("[yellow]Write at least 3 charachters[/]")
        return value


class IDPrompt(PromptBase[int]):
    def process_response(self, value: str) -> int:
        try:
            int_value = int(value)
        except ValueError:
            raise InvalidResponse("[yellow]ID must be a number[/]")

        if int_value <= 0:
            raise InvalidResponse("[yellow]ID must be greater than 0[/]")

        return int_value
