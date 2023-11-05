# a simple integrator class
# A ray is hit and then get the color.
# It is the rendering equation solver.
import RT_utility as rtu
import RT_ray as rtr

class Integrator():
    def __init__(self) -> None:
        pass

    def compute_scattering(self, rGen_ray, scene, maxDepth):
        if maxDepth <= 0:
            # for each light
            # find if light can directly shine on this point
            # return the light color
            return rtu.Color()

        # if the generated ray hits an object
        found_hit = scene.find_intersection(rGen_ray, rtu.Interval(0.000001, rtu.infinity_number))
        if found_hit == True:
            # get the hit info
            hinfo = scene.getHitList()
            # get the material of the object
            hmat = hinfo.getMaterial()
            # compute scattering
            sinfo = hmat.scattering(rGen_ray, hinfo)
            # if no scattering (It is a light source)
            if sinfo is None:
                # return Le
                return hmat.emitting()  
            # return the color
            return self.compute_scattering(rtr.Ray(hinfo.getP(), sinfo.scattered_ray.getDirection()), scene, maxDepth-1) * sinfo.attenuation_color

        # previous background color
        # return scene.get_sky_background_color(rGen_ray)
        return scene.getBackgroundColor()

