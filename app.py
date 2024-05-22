from flask import Flask, send_file, request, jsonify, render_template

from src.core.application.userCases.userUseCase import UserUseCase
from src.core.domain.services.userService import UserService
from src.adapter.driven.userRepository import UserRepository
from src.adapter.driver.controller import Controller

userRepository = UserRepository()
userUseService = UserService(userRepository)
userUseCase = UserUseCase(userUseService)
controller = Controller(userUseCase) 

app = Flask(__name__)

@app.route('/create', methods=["GET"])
def create():
    return controller.createUser(request)

app.run(debug=True)