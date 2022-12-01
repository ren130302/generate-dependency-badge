# Generate Dependency Badge
```yml
name: 'Generate Dependency Badge'

on:
  push:
    paths: ["pom.xml"]
  workflow_dispatch:

jobs:
  generate-dependency-badge:
    runs-on: ubuntu-latest
    
    steps:
    - name: 'Generate Dependency Badge'
      uses: ren130302/generate-dependency-badge@v1
```

Required description in README.md
```md
<!-- start dependencies -->
<!-- end dependencies -->
```
