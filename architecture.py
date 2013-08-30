"""
A very basic overview of how the car will be architected. 

Please fork and update the architecture code.

Source: https://gist.github.com/blindmonkey/6156477
"""

class Car:
  def detect_lanes(self):
    # Use computer vision to detect the lanes around the car.
    
  def get_pending_collisions(self):
    # Use computer vision to detect all objects moving toward the car (relative to the car's speed), and their relative speeds
    return collisions
  
  def get_current_direction(self):
    # Returns the direction that the car is currently going in, as well as the forces being applied wherever relevant
    return direction
  
  def modify_direction_according_to_lanes(direction, lanes):
    # Modifies the direction variable according to lanes such that in the next 'frame', the car will
    # move to stay within the lane bounds.
    return modified_direction
  
  def modify_direction_according_to_collisions(direction, collisions):
    # Modifies the direction variable according to collisions that are about to happen.
    # If no clean escape route can be identified the goal is to minimize damage.
    return modified_direction
    
  def apply_direction(self, direction):
    # Given the delta between the new direction and the current direction, applies forces
    # to the wheel, brakes, and gas such that the new direction either becomes the current
    # direction or will become the new direction within the next n frames.
  
  def drive(self):
    lanes = self.detect_lanes()
    collisions = self.get_pending_collisions()
    new_direction = self.get_current_direction()
    if lanes:
      new_direction = self.modify_direction_according_to_lanes(new_direction, lanes)
    if collisions:
      new_direction = self.modify_direction_according_to_collisions(new_direction, collisions)
    self.apply_direction(new_direction)
    
  def drive_loop(self):
    while self.driving:
      self.drive()
