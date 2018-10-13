'''
customproblem import statement
'''
name = "customproblem"

from .customproblem import College, Department, Member, Professor, Student

__all__ = ['College', 'Department', 'Member', 'Professor', 'Student']
