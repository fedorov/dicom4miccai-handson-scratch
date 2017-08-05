import numpy as np

class SeriesGeometryChecker:

  # initialize with a pandas data frame containing series attributes
  # Columns that are expected to be present:
  #  - ImagePositionPatient
  #  - ImageOrientationPatient
  #  - SOPInstanceUID
  def __init__(self, series_df, warnings=False):
    self.series_df = series_df
    self.epsilon = 0.01
    self.computedSliceThickness = np.NaN
    self.warnings=warnings
    return
  #
  # now for each series and subseries, sort the images
  # by position and check for consistency
  #

  # TODO: more consistency checks:
  # - is there gantry tilt?
  # - are the orientations the same for all slices?
  def geometryOK(self):
    #
    # use the first file to get the ImageOrientationPatient for the
    # series and calculate the scan direction (assumed to be perpendicular
    # to the acquisition plane)
    #

    validGeometry = True
    ref = {}
    positions = []
    orientations = []
    for tag in ["ImagePositionPatient", "ImageOrientationPatient"]:
      for value in self.series_df[tag]:
        if not value or value == "NA":
          return False
        if tag == "ImagePositionPatient":
          positions.append(np.array([float(zz) for zz in value.split('/')]))
        if tag == "ImageOrientationPatient":
          orientations.append(np.array([float(zz) for zz in value.split('/')]))

    # get the geometry of the scan
    # with respect to an arbitrary slice
    refPosition = positions[0]
    refOrientation = orientations[0]

    x = refOrientation[:3]
    y = refOrientation[3:]

    scanAxis = np.cross(x,y)

    #
    # for each file in series, calculate the distance along
    # the scan axis, sort files by this
    #
    sortList = []
    for p,o in zip(positions,orientations):
      dist = np.dot(p-refPosition, scanAxis)
      #print(dist)
      sortList.append((self.series_df["SOPInstanceUID"],dist))

    sortList = sorted(sortList, key=lambda x: x[1])

    # confirm equal spacing between slices
    dist0 = sortList[1][1]-sortList[0][1]
    for i in range(len(sortList))[1:]:
      distN = sortList[i][1]-sortList[i-1][1]
      #print(str(sortList[i]))
      #print(distN)
      distDiff = distN-dist0
      if distDiff > self.epsilon:
        if self.warnings:
          print("Images are not equally spaced. Difference of %g in spacing detected!" % (distDiff))
        return False

    self.computedSliceThickness = dist0
    return True
