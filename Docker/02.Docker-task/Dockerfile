# === Stage 1: Build the application ===
FROM maven:3.8.8-eclipse-temurin-11 AS build
# Set the working directory inside the container
WORKDIR /app
# Copy the necessary files for the build process
COPY myapp/demo/pom.xml .
COPY myapp/demo/src ./src 
# Build the project without running tests
RUN mvn clean package -DskipTests

# === Stage 2: Run the application ===
FROM eclipse-temurin:11-jre-jammy
# Set the working directory
WORKDIR /app
# Copy the compiled JAR file from the previous stage
COPY --from=build /app/target/*.jar ./app.jar
# Expose port (change if your app uses a different one)
EXPOSE 8080
# Run the application
ENTRYPOINT ["java", "-jar", "app.jar"]

