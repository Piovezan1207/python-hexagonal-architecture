from flask import Flask, send_file, request, jsonify, render_template

from src.core.application.services.userService import UserService
from src.adapter.driven.userRepository import UserRepository
from src.adapter.driver.controller import Controller

userUseService = UserService(UserRepository())
controller = Controller(userUseService)

app = Flask(__name__)

@app.route('/create', methods=["GET"])
def create():
    return controller.createUser(request)

app.run(debug=True)