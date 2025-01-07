import 'package:http/http.dart' as http;
import 'dart:convert';

class ApiService {
  static const String apiUrl = 'https://your-api-url';

  Future<Map<String, dynamic>> registerUser(String username, String email, String password) async {
    final response = await http.post(
      Uri.parse('$apiUrl/register/'),
      body: json.encode({'username': username, 'email': email, 'password': password}),
      headers: {'Content-Type': 'application/json'},
    );
    return json.decode(response.body);
  }

  Future<Map<String, dynamic>> getProducts() async {
    final response = await http.get(Uri.parse('$apiUrl/products/'));
    return json.decode(response.body);
  }
}


import 'package:flutter/material.dart';
import 'services/api_service.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  final ApiService apiService = ApiService();

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Ashker Credit',
      home: Scaffold(
        appBar: AppBar(title: Text("API Service with Dio")),
        body: FutureBuilder(
          future: apiService.getData("https://example.com/api/endpoint"),
          builder: (context, snapshot) {
            if (snapshot.connectionState == ConnectionState.waiting) {
              return Center(child: CircularProgressIndicator());
            } else if (snapshot.hasError) {
              return Center(child: Text('Error: ${snapshot.error}'));
            } else {
              return Center(child: Text('Data: ${snapshot.data}'));
            }
          },
        ),
      ),
    );
  }
}
