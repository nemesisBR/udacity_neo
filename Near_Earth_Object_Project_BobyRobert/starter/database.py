from models import OrbitPath, NearEarthObject
import pandas as pd
#temp = pd.read_csv(r'data/neo_data.csv')

#temp2 = temp.describe()



class NEODatabase(object):
    """
    Object to hold Near Earth Objects and their orbits.

    To support optimized date searching, a dict mapping of all orbit date paths to the Near Earth Objects
    recorded on a given day is maintained. Additionally, all unique instances of a Near Earth Object
    are contained in a dict mapping the Near Earth Object name to the NearEarthObject instance.
    """

    def __init__(self, filename):
        """
        :param filename: str representing the pathway of the filename containing the Near Earth Object data
        """
        # TODO: What data structures will be needed to store the NearEarthObjects and OrbitPaths?
        # TODO: Add relevant instance variables for this.
        self.filename = filename
        self.df = None
        self.neo_name = dict()
        self.orbit_date = dict()

    def load_data(self, filename=None):
        """
        Loads data from a .csv file, instantiating Near Earth Objects and their OrbitPaths by:
           - Storing a dict of orbit date to list of NearEarthObject instances
           - Storing a dict of the Near Earth Object name to the single instance of NearEarthObject

        :param filename:
        :return:
        """

        if not (filename or self.filename):
            raise Exception('Cannot load data, no filename provided')

        filename = filename or self.filename

        # TODO: Load data from csv file.
        # TODO: Where will the data be stored?
        
        self.df = pd.read_csv(filename)
        
        for i in range(self.df.shape[0]):
            name = self.df['name'][i]
            
            
            
            if name in self.neo_name:
                self.neo_name[name].update_orbits(self.df.iloc[i])
                
            else:
                temp = NearEarthObject()
                temp.fill_data(self.df.iloc[i])
                self.neo_name[name] = temp
                self.neo_name[name].update_orbits(self.df.iloc[i])
                
            date = self.df['close_approach_date'][i]
            
            if date in self.orbit_date:
                temp2 = OrbitPath()
                temp2.update_param(self.df.iloc[i])
                self.orbit_date[date].append(temp2)
            else:
                temp2 = OrbitPath()
                temp2.update_param(self.df.iloc[i])
                self.orbit_date[date] = [temp2]
            
        return None