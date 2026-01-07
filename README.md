# RT-python-week05
Ray tracing course week 05

This repository is for 'Raytracing in Entertainment Industry' (01418283).
This course is set to be taught for undergrad students at Dept of Computer Science, Faculty of Science, Kasetsart University.
The codes were rewritten and modified from https://raytracing.github.io/books/RayTracingInOneWeekend.html.

**Prerequisites :**
1. C/C++ or python.
2. Object-Oriented Programming (OOP).
3. Linear algebra for undergrad students.


**Class assignment**

1. Implement direct lighting effect in the 'compute_scattering()' method. As of now, the direct lighting only handle point lights. Do not forget to submit your modify code.
2. Add a point light source (white color [1.0,1.0,1.0]) at the location (0,0,0) and render it with the scene in 'renderPointLight()'. Submit your rendered result. (week05_point_light.png)
3. Keep quad patches on the left and the right (remove the rest). Keep the point light at the location (0,0,0). Render it and submit the rendered result.
4. Explain why the result from (3.) has different illumination compared to (2.).
5. Add a render function called 'renderPointLightShadow()' using (2). Changing the location of the point light to (4,0,0). Render the scene and explain the rendered result. Do not forget to submit your rendered result.
6. Create a scene containing spheres and quads then light the scene up with a point light. Do not forget to submit your rendered result.
