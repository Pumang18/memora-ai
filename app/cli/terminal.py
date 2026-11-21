from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt

from app.services.chat_service import ChatService


class TerminalApp:

    def __init__(self):

        self.console = Console()
        self.chat_service = ChatService()

    def start(self):

        self.console.print(
            Panel(
                "[bold cyan]MEMORA AI[/bold cyan]\n"
                "Your Personal AI Assistant",
                border_style="cyan"
            )
        )

        self.console.print(
            "[green]Gemini connection initialized![/green]"
        )

        try:

            while True:

                user_input = Prompt.ask(
                    "\n[bold green]You[/bold green]"
                ).strip()

                if not user_input:
                    continue

                if user_input == "/exit":
                    break

                if user_input == "/clear":

                    self.chat_service.clear_history()

                    self.console.print(
                        "[yellow]History cleared.[/yellow]"
                    )

                    continue

                with self.console.status(
                    "[cyan]Memora is thinking..."
                ):

                    result = self.chat_service.chat(
                        user_input
                    )

                self.console.print(
                    Panel(
                        result["content"],
                        title="Memora AI",
                        border_style="blue"
                    )
                )

                self.console.print(
                    f"[dim]Model: {result['model']} | "
                    f"Input: {result['input_tokens']} | "
                    f"Output: {result['output_tokens']} | "
                    f"Total: {result['total_tokens']}[/dim]"
                )

        except KeyboardInterrupt:

            self.console.print(
                "\n[yellow]Exiting Memora AI...[/yellow]"
            )

        except Exception as error:

            self.console.print(
                f"[red]Application error: {error}[/red]"
            )

        finally:

            self.chat_service.close()

            self.console.print(
                "[green]Memora AI closed.[/green]"
            )