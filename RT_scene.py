# Scene class
import RT_utility as rtu
import numpy as np

class Scene:
    def __init__(self, cBgcolor=rtu.Color(0.01,0.01,0.01)) -> None:
        self.obj_list = []
        self.hit_list = None
        self.background_color = cBgcolor
        self.light_list = []
        pass

    def add_object(self, obj):
        self.obj_list.append(obj)

    def find_intersection(self, vRay, cInterval):

        np_obj_list = np.array(self.obj_list)
        found_hit = False
        # initialize the closet maximum of t
        closest_tmax = cInterval.max_val
        hinfo = None
        # for each object in the given scene
        for obj in np_obj_list:
            # get the hit info from the intersection between an object and the given ray.
            hinfo = obj.intersect(vRay, rtu.Interval(cInterval.min_val, closest_tmax))
            # if the object is hit by the given ray.
            if hinfo is not None:
                # update the closet maximum of t
                # update the hit list
                closest_tmax = hinfo.getT()
                found_hit = True
                self.hit_list = hinfo
        # return if found any hit or not
        return found_hit


    def getHitNormalAt(self, idx):
        return self.hit_list[idx].getNormal() 
    
    def getHitList(self):
        return self.hit_list

    def getBackgroundColor(self):
        return self.background_color

    def get_sky_background_color(self, rGen_ray):
        unit_direction = rtu.Vec3.unit_vector(rGen_ray.getDirection())
        a = (unit_direction.y() + 1.0)*0.5
        return rtu.Color(1,1,1)*(1.0-a) + rtu.Color(0.5, 0.7, 1.0)*a
    
    def find_lights(self):
        np_obj_list = np.array(self.obj_list)
        for obj in np_obj_list:
            if obj.material.is_light():
                self.light_list.append(obj)


