from rest_framework import serializers

class FlowCellResultSerializer(serializers.Serializer):
    """
    Serializer for FlowCell result data.

    This serializer is responsible for serializing the results of a FlowCell 
    process, which includes the number of qualifying cells and their coordinates.

    Attributes:
        qualifying_cells (int): The number of cells that meet the qualification criteria.
        coordinates (list of list of int): A list containing the coordinates of 
                                           the qualifying cells. Each coordinate is 
                                           represented as a list of two integers 
                                           [x, y], indicating the position of the cell.
    """
    
    qualifying_cells = serializers.IntegerField()
    coordinates = serializers.ListField(
        child=serializers.ListField(
            child=serializers.IntegerField()
        )
    )
