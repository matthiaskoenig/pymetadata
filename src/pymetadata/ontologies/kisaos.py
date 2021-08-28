"""Working with the KISAO ontology."""

import logging
import re
from collections import namedtuple
from enum import Enum, unique
from typing import Dict

from kisao import Kisao
from kisao.data_model import IdDialect
from pronto import Ontology, Term


logger = logging.getLogger(__name__)

kisao_ontology = Kisao()
kisao_pattern = re.compile(r"^KISAO_\d{7}$")


def create_kisao_lookup() -> Dict[str, str]:
    """Create dictionary for lookup by name."""
    pronto_ontology: Ontology = kisao_ontology._ontology
    name_to_kisao: Dict[str, str] = {}
    for term_id in pronto_ontology:
        if "KISAO#_KISAO_" in term_id:
            logger.warning(f"Incorrect kisao id: {term_id}")
            continue
        try:
            kisao_id = kisao_ontology.get_normalized_id(
                term_id.split("#")[1], dialect=IdDialect.kisao
            )
            term: Term = kisao_ontology.get_term(kisao_id)
            name = term.name
            if name in name_to_kisao:
                raise ValueError
            name_to_kisao[name] = kisao_id
        except (KeyError, ValueError) as err:
            logger.warning(f"{err}")

    return name_to_kisao


kisao_lookup = create_kisao_lookup()


def validate_kisao(kisao: str) -> str:
    """Validate and normalizes kisao id against pattern."""
    if not kisao.startswith("KISAO"):
        # try lookup by name
        kisao = kisao_lookup.get(kisao, kisao)

    if kisao.startswith("KISAO:"):
        kisao = kisao.replace(":", "_")

    if not re.match(kisao_pattern, kisao):
        raise ValueError(
            f"kisao '{kisao}' does not match kisao pattern " f"'{kisao_pattern}'."
        )

    # term = kisao_ontology.get_term(kisao)
    # check that term exists

    return kisao


def name_kisao(kisao: str, name: str = None) -> str:
    """Get name for kisao id."""
    term: Term = kisao_ontology.get_term(kisao)
    if not term:
        raise ValueError(f"No term in kisao ontology for: '{kisao}'")

    kisao_name = term.name
    if kisao_name != term.name:
        logger.warning(f"Name '{name}' does not match kisao name '{kisao_name}'")
    if name:
        return name
    else:
        return kisao_name
