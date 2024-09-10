# flowcells/views.py
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .dataProcessing.google_sheet_utils import get_google_sheet_data, authenticate_and_get_credentials
from .dataProcessing.find_flow_cells import find_flow_cells
from .serializers import FlowCellResultSerializer

class FlowCellView(APIView):
    """
    Class-based view to handle flow cell calculations for different cases.
    
    This view is designed to process flow cell data for a specific case (represented by `case_number`) 
    by fetching data from a Google Sheet, processing it to find qualifying cells, and returning the results.

    Workflow:
    1. Authenticate and connect to Google Sheets API to retrieve the relevant sheet data for the given case.
    2. Process the sheet data to identify and return the qualifying flow cells and their coordinates.
    3. Return the results as an HTTP response, either in serialized form or as an error message if any failure occurs.
    """

    def get(self, request, case_number):
        """
        Handle GET requests for a specific case, identified by `case_number`.

        Args:
            request: The incoming HTTP request object.
            case_number: The case identifier (integer), which is used to determine which Google Sheet to fetch data from.

        Returns:
            Response: An HTTP response containing either the results (qualifying flow cells) 
                      or an error message if something went wrong.

        Steps:
        1. The method begins by specifying the ID of the Google Sheet to access (`spreadsheet_id`).
        2. It authenticates the service using the `authenticate_and_get_credentials` function and then 
           retrieves the relevant sheet data for the requested case number using `get_google_sheet_data`.
        3. If the data fetch fails, it returns a 500 HTTP response with an error message.
        4. If the data fetch is successful, the data is processed using the `find_flow_cells` function, 
           which returns the qualifying flow cells' coordinates.
        5. The number of qualifying cells and their coordinates are then wrapped in a dictionary as `response_data`.
        6. The result is serialized (using `FlowCellResultSerializer`) and returned as an HTTP response.

        Error Handling:
        If the Google Sheets data cannot be fetched, a 500 Internal Server Error is returned with an appropriate error message.
        """
        spreadsheet_id = '1guE4DI4wQpBXPlXRKXVEeb3nH84Phq6YqgYK9M4NUT0'  # Replace with your actual sheet ID
        
        # Step 1: Authenticate and get Google Sheets data
        creds = authenticate_and_get_credentials()
        sheet_name = f'case {case_number}'  # Specify the sheet name dynamically based on the case number
        sheet_data = get_google_sheet_data(spreadsheet_id, sheet_name, creds)  # Fetch the sheet data

        # Step 2: Check if sheet data retrieval was successful
        if sheet_data is None:
            # If the data fetch failed, return an error response
            return Response({'error': 'Failed to fetch data from Google Sheets'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        # Step 3: Process the data to find qualifying cells
        result = find_flow_cells(sheet_data)  # Process the sheet data to get qualifying cell coordinates
        print(result)  # Debugging: Print the result to the console for verification (can be removed in production)

        # Step 4: Create response data dictionary
        response_data = {
            'qualifying_cells': len(result),  # Number of qualifying cells found
            'coordinates': result  # Coordinates of the qualifying cells
        }

        # Step 5: Serialize the response data using FlowCellResultSerializer
        serializer = FlowCellResultSerializer(response_data)
        return Response(serializer.data)  # Return serialized data as the HTTP response
