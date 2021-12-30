# Python Playground

Use python3 to run the scripts

## Encode and decode a string

```bash
klaus@MBP-von-Klaus ~/python_playground
$ python3 encode_decode.py -e 'ich und du müllers kuh'
encode: Input=ich und du müllers kuh
encode: Output=jdi0voe0ev0nßmmfst0lvi
```

```bash
klaus@MBP-von-Klaus ~/python_playground
$ python3 encode_decode.py 'jdi0voe0ev0nßmmfst0lvi'
decode: Input=jdi0voe0ev0nßmmfst0lvi
decode: Output=ich und du müllers kuh
```

## Measure execution time of function using decorator

```bash
$ python3 measure.py
Function took 2.0002150535583496 seconds to run
```