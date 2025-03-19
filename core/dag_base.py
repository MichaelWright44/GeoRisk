# DAG base class implementation

# Standard Imports
import logging
from typing import Dict, List

# Local Imports

# Third Party Imports
import numpy as np
import pandas as pd


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getlogger(__name__)


#TODO: Define data class specifications based off of input from: https://eccc-msc.github.io/open-data/msc-datamart/readme_en/

class Node:
    """Base class for nodes in the DAG."""

    def __init__(self, node_id: str, dependencies: List[str] = None):
        self.node_id = node_id
        self.dependencies = dependencies or []
        self.data = None
        self.completed = False
        self.error = None

        async def execute(self, input_data):
            try:
                if input_data is None:
                    input_data = {}
                logger.info(f"Executing node: {self.node_id}")
                self.data = await self._process(input_data)
                self.completed = True
                return self.data
            except Exception as e:
                self.error = str(e)
                logger.error(f"Error in node {self.node_id}: {self.error}")

        async def _process(self, input_data):
            """subclass base method that needs to be implemented on a per node basis."""
            raise NotImplementedError



# I wonder if an interesting way to do this is actually to use a grid that takes elevation data, date, and the previous rolling
# 5 days of precipitation data and guesses what the water accumulation will be for the next day.
# This would be a form of machine learning that is applied to each grid cell using historical data for training.
# The grid could then be used to predict water accumulation for any given location and time.

class _calculate_water_accumulation(Node):
    """Node for calculating water accumulation based on precipitation and elevation."""

    def __init__(self, node_id: str = "calculate_water_accumulation"):
        super().__init__(node_id, dependencies=["fetch_precipitation", "fetch_elevation"])
        #TODO: first thing to do here is actually going to be to define the grid and data structure to hold this.


        
        
        

