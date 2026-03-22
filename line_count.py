import sys
from pyspark import SparkContext

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: line_count.py <input_dir> <output_dir>")
        sys.exit(-1)

    sc = SparkContext(appName="RepoLineCount")
    
    files = sc.wholeTextFiles(sys.argv[1])
    
    line_counts = files.map(lambda file_data: f'"{file_data[0].split("/")[-1]}": {len(file_data[1].splitlines())}')
    
    line_counts.coalesce(1).saveAsTextFile(sys.argv[2])
    
    sc.stop()