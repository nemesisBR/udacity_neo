class NearEarthObject(object):
    """
    Object containing data describing a Near Earth Object and it's orbits.

    # TODO: You may be adding instance methods to NearEarthObject to help you implement search and output data.
    """

    def __init__(self, **kwargs):
        """
        :param kwargs:    dict of attributes about a given Near Earth Object, only a subset of attributes used
        """
        # TODO: What instance variables will be useful for storing on the Near Earth Object?
        
        self.id = None
        self.name = None
        self.url = None
        self.abs_mag = None
        self.diameter_min_km = None
        self.diameter_max_km = None
        self.diameter_min_mtr = None
        self.diameter_max_mtr = None
        self.diameter_min_mil = None
        self.diameter_max_mil = None
        self.diameter_min_feet = None
        self.diameter_max_feet = None
        self.is_potentially_hazardous_asteroid = None
        self.cad = None
        self.cad_full = None
        
        self.close_approach_date = None
        self.close_approach_date_full = None
        self.miss_distance_astronomical = None
        self.miss_distance_lunar = None
        self.miss_distance_kilometers = None
        self.miss_distance_miles = None
        self.orbiting_body = None
        
        self.orbits = []
        
    def fill_data(self,kwargs):
        
        self.id = kwargs['id']
        self.name = kwargs['name']
        self.url = kwargs['nasa_jpl_url']
        self.abs_mag = kwargs['absolute_magnitude_h']
        self.diameter_min_km = kwargs['estimated_diameter_min_kilometers']
        self.diameter_max_km = kwargs['estimated_diameter_max_kilometers']
        self.diameter_min_mtr = kwargs['estimated_diameter_min_meters']
        self.diameter_max_mtr = kwargs['estimated_diameter_max_meters']
        self.diameter_min_mil = kwargs['estimated_diameter_min_miles']
        self.diameter_max_mil = kwargs['estimated_diameter_max_miles']
        self.diameter_min_feet = kwargs['estimated_diameter_min_feet']
        self.diameter_max_feet = kwargs['estimated_diameter_max_feet']
        self.is_potentially_hazardous_asteroid = kwargs['is_potentially_hazardous_asteroid']
        self.cad = kwargs['close_approach_date']
        self.cad_full = kwargs['close_approach_date_full']
        
        self.close_approach_date = kwargs['close_approach_date']
        self.close_approach_date_full = kwargs['close_approach_date_full']
        self.miss_distance_astronomical = kwargs['miss_distance_astronomical']
        self.miss_distance_lunar = kwargs['miss_distance_lunar']
        self.miss_distance_kilometers = kwargs['miss_distance_kilometers']
        self.miss_distance_miles = kwargs['miss_distance_miles']
        self.orbiting_body = kwargs['orbiting_body']
        

    def update_orbits(self, orbit):
        """
        Adds an orbit path information to a Near Earth Object list of orbits

        :param orbit: OrbitPath
        :return: None
        """

        # TODO: How do we connect orbits back to the Near Earth Object?
        temp2 = OrbitPath()
        temp2.update_param(orbit)
        self.orbits.append(temp2)


class OrbitPath(object):
    """
    Object containing data describing a Near Earth Object orbit.

    # TODO: You may be adding instance methods to OrbitPath to help you implement search and output data.
    """

    def __init__(self, **kwargs):
        """
        :param kwargs:    dict of attributes about a given orbit, only a subset of attributes used
        """
        self.neo_name = None
        self.kmps = None
        self.kmph = None
        self.mph = None
        self.close_approach_date = None
        self.close_approach_date_full = None
        self.miss_distance_astronomical = None
        self.miss_distance_lunar = None
        self.miss_distance_kilometers = None
        self.miss_distance_miles = None
        self.orbiting_body = None
        
        # TODO: What instance variables will be useful for storing on the Near Earth Object?
    def update_param(self,kwargs):
        
        self.neo_name = kwargs['name']
        self.kmps = kwargs['kilometers_per_second']
        self.kmph = kwargs['kilometers_per_hour']
        self.mph = kwargs['miles_per_hour']
        self.close_approach_date = kwargs['close_approach_date']
        self.close_approach_date_full = kwargs['close_approach_date_full']
        self.miss_distance_astronomical = kwargs['miss_distance_astronomical']
        self.miss_distance_lunar = kwargs['miss_distance_lunar']
        self.miss_distance_kilometers = kwargs['miss_distance_kilometers']
        self.miss_distance_miles = kwargs['miss_distance_miles']
        self.orbiting_body = kwargs['orbiting_body']
