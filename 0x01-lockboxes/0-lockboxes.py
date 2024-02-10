#!/usr/bin/python3

"""
Module to solve the lockboxing algorithm.
"""


def canUnlockAll(boxes):
    """
    Check if all boxes have keys to other
    boxes.
    """
    box_count = len(boxes)
    opened_boxes = set([0])
    closed_boxes = set(boxes[0]).difference(set([0]))
    while len(closed_boxes) > 0:
        boxId = closed_boxes.pop()
        if not boxId or boxId >= box_count or boxId < 0:
            continue
        if boxId not in opened_boxes:
            closed_boxes = closed_boxes.union(boxes[boxId])
            opened_boxes.add(boxId)
    return box_count == len(opened_boxes)
