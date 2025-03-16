# Run unit tests

## Navigate back to root directory

cd c:\Users\user\Documents\GitHub\algo\dotnet

## Run all tests

```zsh
    dotnet clean
    dotnet restore
    dotnet build
    dotnet test
```

## Run specific test class

```zsh
    dotnet test --filter "RankedUnionTests"
```
