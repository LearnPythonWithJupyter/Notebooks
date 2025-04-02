#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 12:25:45 2025

@author: serenabonaretti

This module contains functions to create usernames and passwords
"""

import random


def create_username (first_name, last_name):
    """Create a lowercase username made of initial of first name and last name
    
    Parameters
    ----------
    first_name: string 
        First name of a person
    last_name: string
        Last name of a person
        
    Returns    
    -------
    username: string
        Created username      
    """
    
    # concatenate initial of first name and last name
    username = first_name[0] + last_name
    # make sure username is lowercase
    username = username.lower()
    
    # return username
    return username


def create_password():
    """Create a password composed of four random integers 
        
    Returns    
    -------
    password: string
        Created password  
    """
    
    # create a random number with four digits
    password = str(random.randint(1000,9999))
     
    # return password
    return password


def create_database (customers): 
    """Creates a database as a dictionary with usernames as keys and passwords as values  
    
    Parameters
    ----------
    customers : list of lists
        Each sublist contains first name and last name of a customer
        
    Returns    
    -------
    db : dictionary
        Created database (shorted as db)
    n_customers : int
        Number of customers in the database
    """
    
    # initialize dictionary (i.e. database)
    db = {}
    
    # for each customer
    for customer in customers:

        # create username
        username = create_username (customer[0], customer[1])

        # create password
        password = create_password()  
        
        # add username and password to db
        db[username] = password
        
    # compute number of customers 
    n_customers = len(db)

    # return dictionary and its length
    return db, n_customers


if __name__ == "__main__":
    
    # input to the main function
    customers = [["Maria", "Lopez"], ["Julia", "Smith"], ["Mohammed", "Seid"]] 
    
    # create the database
    database, number_customers = create_database(customers)
    
    # print the outputs
    print ("Database:", database)
    print ("Number of customers:", number_customers)            

    
    
    
    
    
    
    