import create_bbox_files as bbox
import create_subsets as subsets
import crop as crop
import insert_categories_name as insert
import height_width as size


#insert.insertCategoriesInFile()
size.createSizeFile()
size.eliminateCategoriesWithSmallBBox()
subsets.createBigDataFile()
#bbox.createCoordinatesFileFromSubset()
#crop.cropImages()