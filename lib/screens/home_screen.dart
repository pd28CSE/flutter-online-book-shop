import 'package:flutter/material.dart';
import 'package:firebase_core/firebase_core.dart';
import 'package:firebase_auth/firebase_auth.dart';
import 'package:provider/provider.dart';
import '../firebase_options.dart';

import 'product_overview_screen.dart';
import '../providers/user_provider.dart';
import './verify_email_screen.dart';
import './login_screen.dart';
import './loading_screen.dart';

class HomeScreen extends StatelessWidget {
  static const routeName = 'home-screen';
  const HomeScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return FutureBuilder(
      future: Firebase.initializeApp(
          options: DefaultFirebaseOptions.currentPlatform),
      builder: (context, snapshot) {
        switch (snapshot.connectionState) {
          case ConnectionState.none:
            return const Text('None');
          case ConnectionState.waiting:
            return const LoginScreen();
          case ConnectionState.active:
            return const Text('Active');
          case ConnectionState.done:
            final user = FirebaseAuth.instance.currentUser;
            if (user != null) {
              // debugPrint('--Email is Verified');
              // if (user != null) {
              // debugPrint('--You are Verified User.');
              // debugPrint('--$user');
              Provider.of<UserProvider>(context)
                  .fetchUser(user.email as String);
              return const NotesScreen();
              // } else {
              //   // debugPrint('--You Need Verify  Your Email First.');
              //   // return const VerifyEmailScreen();
              // }
            } else {
              return const LoginScreen();
            }
          default:
            // debugPrint('--Default, Loading ...');
            return const LoadingScreen();
        }
      },
    );
  }
}
