import source.module_particle_systems as m_particle_systems

from . import GenericEntity


class ParticleSystem(GenericEntity):
    tag = 'psys'
    raw_objects = m_particle_systems.particle_systems

    def __init__(self, index, id, flags, system, n_particles, lifetime, damping,
                 gravity, turbulence_size, turbulence_strength,
                 alpha1, alpha2, red1, red2, green1, green2, blue1, blue2, scale1, scale2,
                 box_size, velocity, dir_randomness, rot_speed=0, rot_damping=0):
        super(ParticleSystem, self).__init__(index, id)
        self._flags = flags
        self._system = system
        self._n_particles = n_particles
        self._lifetime = lifetime
        self._damping = damping
        self._gravity = gravity
        self._turbulence_size = turbulence_size
        self._turbulence_strength = turbulence_strength
        self._alpha = (alpha1, alpha2)
        self._red = (red1, red2)
        self._green = (green1, green2)
        self._blue = (blue1, blue2)
        self._scale = (scale1, scale2)
        self._box_size = box_size
        self._velocity = velocity

        self._dir_randomness = dir_randomness
        self._rot_speed = rot_speed
        self._rot_damping = rot_damping

    def export(self, compiler):
        result = "%s %d %s  %d %f %f %f %f %f \n" % \
                 (self._id, self._flags, self._system, self._n_particles,
                  self._lifetime, self._damping, self._gravity,
                  self._turbulence_size, self._turbulence_strength)
        for x in (self._alpha, self._red, self._green, self._blue, self._scale):
            result += "%f %f   %f %f\n" % (x[0][0], x[0][1], x[1][0], x[1][1])

        result += "%f %f %f   " % tuple(self._box_size)
        result += "%f %f %f   " % tuple(self._velocity)
        result += "%f \n" % self._dir_randomness

        result += "%f %f " % (self._rot_speed, self._rot_damping)
        result += '\n'
        return result
