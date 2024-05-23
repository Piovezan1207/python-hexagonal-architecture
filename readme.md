# Exemplo de arquitetura hexagonal em python

    python-hexagonal-architecture/
    ├── src/
    │    ├── adapter/
    │    │  ├── driven/
    │    │  │  └── userRepository.py
    │    │  └── driver
    │    │     └── controller.py
    │    └── core/
    │    ├── application/
    │    │  ├── ports/
    │    │  │  └── userPort.py
    │    │  └── services/
    │    │     └── userService.py
    │    └── domain
    │        ├── entities
    │        │  └── User.py
    │        └── repositories
    │            └── userRepositoryPort.py
    └── app.py
    └── readmee.md



