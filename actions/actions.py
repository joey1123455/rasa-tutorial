# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List, Union

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class HealthForm(Action):

    def name(self):
        return 'health_form'

    @staticmethod
    def required_slots(tracker):

        if tracker.get_slot('confirm_exercise') == True:
            return ['confirm_excersise', 'exercise', 'sleep', 'diet', 'stress', 'goal']
        else:
            return ['confirm_excersise', 'sleep', 'diet', 'stress', 'goal']

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        return []

    def slot_mappings(self) -> Dict[Text, Union[Dict, list[Dict]]]:
        return {
            'confirm_exercise': [
                self.form_intent(intent="affirm", value=True),
                self.form_intent(intent="deny", value=False),
                self.form_intent(intent="inform", value=True),
            ],
            'sleep': [
                self.form_intent(intent="sleep"),
                self.form_intent(intent="deny", value=None),
            ],
            'diet': [
                self.form_intent(intent="inform"),
                self.form_intent(intent="affirm"),
                self.form_intent(intent="deny"),
            ],
            'goal': [
                self.form_intent(intent="inform"),
            ]
        }