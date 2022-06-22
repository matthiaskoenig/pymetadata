"""This module searches annotation terms from the ontology lookup service.

See https://www.ebi.ac.uk/ols/docs/api -> Search for documentation.

**Milestone 2.2 Develop backend functionality for the annotation search**
The frontend annotation query will be send to the python backend which will query the
various existing web services (Ontology Lookup Service, Bio Ontologies, AnnotateDB)
to fetch the ontology terms. Results will be processed/cached/ranked and returned to
the frontend as ranked results via the JSON annotation format.

TODO: Create a class which allows to search OLS via the REST API.
see for instance
https://www.ebi.ac.uk/ols/api/search?q=glucose


Do something similar for
https://data.bioontology.org/documentation -> Term search

-> (term_id, ontology, label, descriptions);

object.id, object.name, object.meta_id
"""


from asyncio.log import logger
from this import d
from typing import Optional
import requests


class OLSOntology:
    """Python class to receive response from OLS"""

    def __init__(self, id, iri, short_form, obo_id, label, description, ontology_name, onotology_prefix): 
        self.id = id
        self.iri = iri
        self.short_form = short_form
        self.obo_id = obo_id
        self.label: Optional[str] = label
        self.description: Optional[str] = description
        self.ontology_name = ontology_name
        self.ontology_prefix = onotology_prefix


    def process_response(self, response):
        """Parses response into a list and returns it"""
        list = []

        for i in response['response']['docs']:
            if 'label' in i.keys():
                label = i['label']
            else:
                label = ""
            if 'description' in i.keys():
                description = i['description']
            else:
                description = ""
            
            list.append(
                OLSOntology(
                    i['id'],
                    i['iri'],
                    i['short_form'],
                    i['obo_id'],
                    label,
                    description,
                    i['ontology_name'],
                    i['ontology_prefix']
                    )
                )
                
        return list

    def ols_search(self, term, ontology):
        """Performs GET Query to OLS API and returns response stored list of OLSOntology objects"""
        
        query = "https://www.ebi.ac.uk/ols/api/search?q="+term+"&ontology="+ontology
        try:
            response = requests.get(query)
        except requests.HTTPError as err:
            logger.error(err)
            response = {
                "errors":[err],
                "warnings": [],
            }
        response = response.json()
        data = self.process_response(response)

        return data
