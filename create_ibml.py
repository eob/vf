TYPE = 0
NAME = 1
VALUE_IF_PRESENT = 2
QUERY = 3
OCCURS_BELOW = 4
OCCURS_ABOVE = 5
TOLERANCE = 6
IGNORE_CASE = 7
ANGLE = 8
DISTANCE = 9
OFFSET_UNIT = 10
RECT_TOP = 11
RECT_RIGHT = 12
RECT_BOTTOM = 13
RECT_LEFT = 14
RECT_UNIT = 15

with open('dodd-frank-act-addendum-visual-refiner-inputs.csv', 'r') as f:
  content = f.read()
  content = content.replace('\r', '')
  lines = content.split('\n')

  annotations = []
  for line in lines[1:]:
    line = line.split(',')
    annotation = dict(
      type=line[TYPE],
      label=line[NAME],
      relative_geometries=[
        dict(
          text_anchor=dict(
            search_phrase=line[QUERY],
            search_error_tolerance=line[TOLERANCE],
            ignore_case=(line[IGNORE_CASE]=='1'),
            occurs_below=line[OCCURS_BELOW],
            occurs_above=line[OCCURS_ABOVE]
          ),
          offset=dict(
            angle=int(line[ANGLE]),
            distance=float(line[DISTANCE]),
            unit=line[OFFSET_UNIT]
          ),
          relative_rect=dict(
            top=float(line[RECT_TOP]),
            right=float(line[RECT_RIGHT]),
            bottom=float(line[RECT_BOTTOM]),
            left=float(line[RECT_LEFT]),
            unit=line[RECT_UNIT]
          )
        )
      ],
      visual_refiner_value=dict(
        value_if_present=line[VALUE_IF_PRESENT]
      )
    )
    print(annotation)
    annotations.append(annotation)
  
  ibml = dict(
    ibml=dict(
      documents=[
        dict(
          records=[
            dict(
              annotations=annotations
            )
          ]
        )
      ]
    )
  )
  import json
  jsonstr = json.dumps(ibml)
  print("\n\n IBML FILE: \n\n {}".format(jsonstr))

  with open('fields_to_scrape.ibml', 'w') as f2:
    f2.write(jsonstr)

