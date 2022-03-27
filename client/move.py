from vectors import *

class Move:
    def __init__(self, vectors: Vector):
        """Хранит данные движения объекта"""
        self.x = vectors.x
        self.y = vectors.y
        self.movement_vector = Vector()
        self.max_speed = 5
        self.mass = 10
        self.slowing_radius = 50

    def coord(self, vector):
        """Обновляет текущие координаты объекта"""
        new_vector = vector_sum(Vector(self.x, self.y), vector)
        self.x, self.y = new_vector.x, new_vector.y
        return new_vector

    def distance_to_point(self, x_target, y_target):
        """Возвращает растояние до точки"""
        x = x_target-self.x
        y = y_target-self.y
        return math.sqrt(x**2+y**2)

    def sb_seek(self, target_x, target_y):
        """Алгоритм следования в координаты"""
        desired_vector = Vector(target_x - self.x, target_y - self.y)
        if desired_vector.lenght() < 1:
            desired_vector = Vector(0, 0)
        desired_vector = desired_vector.normalized()

        desired_vector = vector_mult(desired_vector, self.max_speed)

        steering_vector = vector_sub(desired_vector, self.movement_vector)
        steering_vector = vector_mult(steering_vector, 1 / self.mass)

        final_vector = vector_sum(self.movement_vector, steering_vector)
        final_vector.normalized()
        final_vector = vector_mult(final_vector, self.max_speed)
        return self.coord(final_vector)

    def sb_flee(self, target_x, target_y):
        """Алгоритм удаления от координат"""
        desired_vector = Vector(self.x - target_x, self.y - target_y)
        desired_vector = desired_vector.normalized()
        desired_vector = vector_mult(desired_vector, self.max_speed)

        steering_vector = vector_sub(desired_vector, self.movement_vector)
        steering_vector = vector_mult(steering_vector, 1 / self.mass)

        final_vector = vector_sum(self.movement_vector, steering_vector)
        final_vector.normalized()
        final_vector = vector_mult(final_vector, self.max_speed)
        return self.coord(final_vector)

    def sb_arrive(self, target_x, target_y):
        """Алгоритм плавного приближения к координатам"""
        desired_vector = Vector(target_x - self.x, target_y - self.y)
        desired_vector = desired_vector.normalized()

        distance_to_target = self.distance_to_point(target_x, target_y)
        if distance_to_target < self.slowing_radius:
            desired_vector = vector_mult(desired_vector, self.max_speed*(distance_to_target/self.slowing_radius))
        else:
            desired_vector = vector_mult(desired_vector, self.max_speed)

        steering_vector = vector_sub(desired_vector, self.movement_vector)
        steering_vector = vector_mult(steering_vector, 1 / self.mass)

        final_vector = vector_sum(self.movement_vector, steering_vector)
        final_vector.normalized()
        final_vector = vector_mult(final_vector, self.max_speed)
        return self.coord(final_vector)
