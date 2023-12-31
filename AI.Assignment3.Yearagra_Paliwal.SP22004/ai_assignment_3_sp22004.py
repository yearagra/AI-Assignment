# -*- coding: utf-8 -*-
"""AI Assignment 3 SP22004.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ovkymyZ5foM1Duvb66VH_VYoPFz3GXe1
"""

!pip install durable-rules

#IMPORTED THE DURANG LIBRARY
from durable.lang import *

#RULES FOR COURESES
with ruleset('Courses'):
#Machine Learning
    @when_all((m.course == 'Machine Learning') & (m.grades == '8') )
    def machinelearning1(c):
        c.assert_fact('Career', { 'field': 'AI-ML' })

    @when_all((m.course == 'Machine Learning') & (m.grades == '9') )
    def machinelearning2(c):
        c.assert_fact('Career', { 'field': 'AI-ML' })

    @when_all((m.course == 'Machine Learning') & (m.grades == '10') )
    def machinelearning3(c):
        c.assert_fact('Career', { 'field': 'AI-ML' })

#Artificail Intelligence
    @when_all((m.course == 'Artificial Intelligence') & (m.grades == '8') )
    def artificialintelligence1(c):
        c.assert_fact('Career', { 'field': 'AI-ML' })

    @when_all((m.course == 'Artificial Intelligence') & (m.grades == '9') )
    def artificialintelligence2(c):
        c.assert_fact('Career', { 'field': 'AI-ML' })

    @when_all((m.course == 'Artificial Intelligence') & (m.grades == '10') )
    def artificialintelligence3(c):
        c.assert_fact('Career', { 'field': 'AI-ML' })

#Advanced Programming
    @when_all((m.course == 'Advanced Programming') & (m.grades == '8') )
    def AdvancedProgramming1(c):
        c.assert_fact('Career', { 'field': 'AP' })

    @when_all((m.course == 'Advanced Programming ') & (m.grades == '9') )
    def AdvancedProgramming2(c):
        c.assert_fact('Career', { 'field': 'AP' })

    @when_all((m.course == 'Advanced Programming') & (m.grades == '10') )
    def AdvancedProgramming3(c):
        c.assert_fact('Career', { 'field': 'AP' })

#Design 
    @when_all((m.course == 'Design') & (m.grades == '8') )
    def AdvancedProgramming1(c):
        c.assert_fact('Career', { 'field': 'Art' })

    @when_all((m.course == 'Design') & (m.grades == '9') )
    def AdvancedProgramming2(c):
        c.assert_fact('Career', { 'field': 'Art' })

    @when_all((m.course == 'Design') & (m.grades == '10') )
    def AdvancedProgramming3(c):
        c.assert_fact('Career', { 'field': 'Art' }) 

    @when_all(+m.subject)
    def output(c):
        print('Fact: {0} {1} {2}'.format(c.m.subject, c.m.predicate, c.m.object))


#RULES FOR CAREER 
with ruleset('Career'):
    @when_all((m.field == 'AI-ML'))
    def ds(d):
        d.assert_fact({ 'subject': 'Machine Learning Researchers' })
        d.assert_fact({ 'subject': 'AI Engineer' })
        d.assert_fact({ 'subject': 'Data Scientist' })
        d.assert_fact({ 'subject': 'Machine Learning Engineer' })
        d.assert_fact({ 'subject': 'Data Mining and Analysis' })

    @when_all((m.field == 'AP'))
    def ap(d):
        d.assert_fact({ 'subject': 'Software Developer' })
        d.assert_fact({ 'subject': 'Web Developer' })
        d.assert_fact({'subject': 'App Developer' })
        d.assert_fact({'subject': 'Data Analyst' })

    @when_all((m.field == 'Art'))
    def art(d):
        d.assert_fact({ 'subject': 'UI Developer' })
        d.assert_fact({ 'subject': 'Web Developer' })
        d.assert_fact({ 'subject': 'UX Developer' })



    @when_all(+m.subject)
    def output(d):
        print('Fact: {0}'.format(d.m.subject))


call1 = input("Courses Done : Machine Learning, Artificial Intelligence, Advanced Programming, Design :- ")
call2 = input("Grades Obtained In A Range Of 1-10 :- ")
assert_fact('Courses', { 'course': call1, 'grades': call2 })

