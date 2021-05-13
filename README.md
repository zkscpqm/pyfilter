# PyFilter

A small, configurable text filtering app

**Note that the pyfilter/src must be set as Source Root!**

### Components

The main text filter comprises multiple independent filters:
 
 - Any Inclusion Filter: A filter that returns true if any of its keywords/key phrases are found in the input text.
 - All Inclusion Filter: A filter that returns true if all of its keywords/key phrases are found in the input text.
 - Exclusion Filter: A filter that returns true if any of its keywords/key phrases are found in the input text, though unlike the Any Inclusion Filter, this will filter out those inputs rather than let them through.
 - Regex Filter: A filter that returns true if any part of the passed input text matches the given regex pattern.

This filter can be used on strings, lists of strings, or files. Soon; webpages

### Usage

The filter can be used as a class or as a standalone gRPC client-server setup.

 - For direct use in a codebase see examples/basic_filtering_example.py
 - For use as a gRPC server see examples/server_example.py (and the accompanying client at examples/client_example.py)

### TODO

 - Support files structured like lists and filter each line individually
 - Unit and Integration testing of gRPC implementation
 - Integration tests for webpage filtering
 - Multi webpage filtering via crawler
