import json
import os
import uuid
import shutil
import logging
from typing import List, Dict, Any
from common_texts.assignment_1 import common_text as common_text_a1

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def load_assignments(file_path: str) -> List[Dict[str, Any]]:
    with open(file_path) as f:
        return json.load(f)

def index_students() -> List[str]:
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    folder = os.path.join(root, 'assignments')
    return [s for s in os.listdir(folder) if s != "sunit" and os.path.isdir(os.path.join(folder, s))]

def place_assignment(student_id: str, assignment_name: str, content: str) -> bool:
    root_folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    student_folder = os.path.join(root_folder, 'assignments', student_id)
    assignment_path = os.path.join(student_folder, assignment_name)
    
    # Check if assignment already exists
    if os.path.exists(assignment_path):
        logger.warning(f"Assignment already exists for student {student_id}. Skipping.")
        return False
        
    try:
        with open(assignment_path, 'w') as file:
            file.write(content)
        logger.info(f"Created new assignment for student {student_id}")
        return True
    except Exception as e:
        logger.error(f"Error placing assignment for {student_id}: {e}")
        return False

def assign_students(assignments: List[Dict], students: List[str], assignment_name: str) -> List[Dict]:
    updated_assignments = []
    assignments_made = 0
    
    for assignment in assignments:
        # Don't modify assignments that already have students
        if 'student_id' in assignment:
            logger.info(f"Assignment already assigned to {assignment['student_id']}. Skipping.")
            updated_assignments.append(assignment)
            continue
            
        # Only assign if we have available students
        if assignments_made < len(students):
            assignment['assignment_id'] = str(uuid.uuid4())
            assignment['student_id'] = students[assignments_made]
            txt = (
                f"{common_text_a1()}\n\n\n\n"
                f"Title: {assignment.get('title', '')}\n\n"
                f"Description: {assignment.get('description', '')}\n\n"
                f"Unique ID: {assignment['assignment_id']}\n"
            )
            if place_assignment(assignment['student_id'], assignment_name, txt):
                assignments_made += 1
                
        updated_assignments.append(assignment)

    # Only save if we made new assignments
    if assignments_made > 0:
        root_folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        file_path = os.path.join(root_folder, 'assignments_master', 'module1_c.json')
        with open(file_path, 'w') as file:
            json.dump(updated_assignments, file, indent=4)
        logger.info(f"Successfully assigned {assignments_made} new assignments")
    else:
        logger.info("No new assignments were made")

    return updated_assignments

def assignment1():
    root_folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    target_path = os.path.join(root_folder, 'assignments_master', 'module1_c.json')
    
    # Only copy if the file doesn't exist at all
    if not os.path.exists(target_path):
        source_path = os.path.join(root_folder, 'assignments_master', 'module1.json')
        shutil.copy(source_path, target_path)
        logger.info("Created new assignments tracking file")
    
    assignments = load_assignments(target_path)
    students = index_students()
    assign_students(assignments, students, "assignment1")

if __name__ == "__main__":
    assignment1()