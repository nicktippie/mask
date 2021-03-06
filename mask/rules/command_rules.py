from mask.utilities.file import load_file_contents
from mask.rules.rule import Rule

from dataclasses import dataclass
from os.path import exists


@dataclass
class AdHocCommandRule(Rule):
    """ Execute a single ad-hoc SQL command against the database server """

    command: str = None

    def validate_instructions(self) -> None:
        super().validate_instructions()
        if self.command is None or self.command == "":
            raise ValueError(f"Ad-hoc command cannot be empty for {self}")

    def execute(self) -> None:
        self.database_gateway.execute_command(command=self.command)


@dataclass
class AdHocScriptRule(Rule):
    """ Execute an ad-hoc SQL script against the database server """

    script: str = None

    def validate_instructions(self) -> None:
        super().validate_instructions()
        if not exists(self.script):
            raise FileNotFoundError(f"Could not find ad-hoc script at '{self.script}' for {self}")

    def execute(self) -> None:
        script_contents = load_file_contents(file_path=self.script)
        self.database_gateway.execute_command(command=script_contents)
