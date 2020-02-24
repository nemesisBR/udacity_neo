from collections import namedtuple
from enum import Enum

from exceptions import UnsupportedFeature
from models import NearEarthObject, OrbitPath

import operator


class DateSearch(Enum):
    """
    Enum representing supported date search on Near Earth Objects.
    """
    between = 'between'
    equals = 'equals'

    @staticmethod
    def list():
        """
        :return: list of string representations of DateSearchType enums
        """
        return list(map(lambda output: output.value, DateSearch))


class Query(object):
    """
    Object representing the desired search query operation to build. The Query uses the Selectors
    to structure the query information into a format the NEOSearcher can use for date search.
    """

    Selectors = namedtuple('Selectors', ['date_search', 'number', 'filters', 'return_object'])
    DateSearch = namedtuple('DateSearch', ['type', 'values'])
    ReturnObjects = {'NEO': NearEarthObject, 'Path': OrbitPath}

    def __init__(self, **kwargs):
        """
        :param kwargs: dict of search query parameters to determine which SearchOperation query to use
        """
        # TODO: What instance variables will be useful for storing on the Query object?
        self.d = kwargs

    def build_query(self):
        """
        Transforms the provided query options, set upon initialization, into a set of Selectors that the NEOSearcher
        can use to perform the appropriate search functionality

        :return: QueryBuild.Selectors namedtuple that translates the dict of query options into a SearchOperation
        """
        #print(self.d)
        try:
            val = [self.d['date']]
        except:
            val = [self.d['start_date'],self.d['end_date']]
        
        try:
            fil = self.d['filter']
        except:
            fil = None
        
        da = self.DateSearch(len(val),val)
        s = self.Selectors(da,self.d['number'],fil,self.d['return_object'])
        #print(s)
        # TODO: Translate the query parameters into a QueryBuild.Selectors object
        return s

class Filter(object):
    """
    Object representing optional filter options to be used in the date search for Near Earth Objects.
    Each filter is one of Filter.Operators provided with a field to filter on a value.
    """
    Options = {
        # TODO: Create a dict of filter name to the NearEarthObject or OrbitalPath property
        'diameter' : 'diameter_min_km',
        'is_hazardous': 'is_potentially_hazardous_asteroid',
        'distance': 'miss_distance_kilometers'
    }

    Operators = {
        
        # TODO: Create a dict of operator symbol to an Operators method, see README Task 3 for hint
            '=' : operator.eq,
            '>=': operator.ge,
            '<=': operator.le,
            '>' : operator.gt,
            '<' : operator.lt
    }

    def __init__(self, field, object,operation, value): #
        """
        :param field:  str representing field to filter on
        :param field:  str representing object to filter on
        :param operation: str representing filter operation to perform
        :param value: str representing value to filter for
        """
        self.field = field
        self.object = object
        self.operation = operation
        
        if value == 'False':
            self.value = False
        elif value == 'True':
            self.value = True
        else:
            self.value = float(value)

    @staticmethod
    def create_filter_options(filter_options):
        """
        Class function that transforms filter options raw input into filters

        :param input: list in format ["filter_option:operation:value_of_option", ...]
        :return: defaultdict with key of NearEarthObject or OrbitPath and value of empty list or list of Filters
        """

        # TODO: return a defaultdict of filters with key of NearEarthObject or OrbitPath and value of empty list or list of Filters

    def apply(self, results):
        """
        Function that applies the filter operation onto a set of results

        :param results: List of Near Earth Object results
        :return: filtered list of Near Earth Object results
        """
        
        temp = []
        
        for item in results:
            opt = getattr(item, self.Options[self.field])
            
            opr = self.Operators[self.operation]
            val = self.value
            if opr(opt,val):
                temp.append(item)
        
        return temp
        # TODO: Takes a list of NearEarthObjects and applies the value of its filter operation to the results


class NEOSearcher(object):
    """
    Object with date search functionality on Near Earth Objects exposed by a generic
    search interface get_objects, which, based on the query specifications, determines
    how to perform the search.
    """

    def __init__(self, db):
        """
        :param db: NEODatabase holding the NearEarthObject instances and their OrbitPath instances
        """
        self.db = db
        # TODO: What kind of an instance variable can we use to connect DateSearch to how we do search?

    def get_objects(self, query):
        """
        Generic search interface that, depending on the details in the QueryBuilder (query) calls the
        appropriate instance search function, then applys any filters, with distance as the last filter.

        Once any filters provided are applied, return the number of requested objects in the query.return_object
        specified.

        :param query: Query.Selectors object with query information
        :return: Dataset of NearEarthObjects or OrbitalPaths
        """
        
        res = []
        obj = query.return_object
        
        
        if obj == 'NEO':
            
            total = query.number
            temp = query.date_search.type
            
            if temp == 1:
            
                for val in self.db.neo_name:
                    
                    neo_temp = self.db.neo_name[val]
                    
                    if neo_temp.cad == query.date_search.values[0]:
                        res.append(self.db.neo_name[val])
                
            else:
                st_date = query.date_search.values[0]
                en_date = query.date_search.values[1]
                
                
                for val in self.db.neo_name:
                    
                    neo_temp = self.db.neo_name[val]
                    
                    if neo_temp.cad >= st_date and neo_temp.cad <= en_date:
                        res.append(self.db.neo_name[val])
            if query.filters != None:
                for filt in query.filters:
                    
                    param = filt.split(':')
                    
                    filter_obj = Filter(param[0],NearEarthObject,param[1],param[2])
                    res = filter_obj.apply(res)
        else:
            
            total = query.number
            temp = query.date_search.type
            if temp == 1:
            
                for val in self.db.orbit_date:
                    
                    
                    if val == query.date_search.values[0]:
                        res.extend(self.db.orbit_date[val])
                
            else:
                st_date = query.date_search.values[0]
                en_date = query.date_search.values[1]
                
                
                for val in self.db.neo_name:
                    
                    
                    
                    if val >= st_date and val <= en_date:
                        res.extend(self.db.orbit_date[val])

                               
        
        
        
                
        
        
        #print(len(res))
        return res if len(res) <= total else res[:total]
        
        
        
        # TODO: This is a generic method that will need to understand, using DateSearch, how to implement search
        # TODO: Write instance methods that get_objects can use to implement the two types of DateSearch your project
        # TODO: needs to support that then your filters can be applied to. Remember to return the number specified in
        # TODO: the Query.Selectors as well as in the return_type from Query.Selectors