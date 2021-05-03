# PyFilter

A small, configurable text filtering app

### Components

The main text filter comprises multiple independent filters:
 
 - Any Inclusion Filter: A filter that returns true if any of its keywords/key phrases are found in the input text.
 - All Inclusion Filter: A filter that returns true if all of its keywords/key phrases are found in the input text.
 - Exclusion Filter: A filter that returns true if any of its keywords/key phrases are found in the input text, though unlike the Any Inclusion Filter, this will filter out those inputs rather than let them through.

This filter can be used on strings, lists of strings, or files. Soon; webpages

### Usage
*See examples*

### TODO

 - Regex support
 - Have a gRPC server which accepts inputs and spits out filtered outputs
 - Add filter capability for things such as "Match red but not reddish"
 - Add exact filtering (maybe regex will fix this?)
 - Support files structured like lists and filter each line individually