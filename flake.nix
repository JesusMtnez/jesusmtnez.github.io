{
  description = "jesusmtnez.es flake";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixpkgs-unstable";

    flake-parts = {
      url = "github:hercules-ci/flake-parts";
      inputs.nixpkgs-lib.follows = "nixpkgs";
    };

    theme = {
      url = "github:luizdepra/hugo-coder";
      flake = false;
    };
  };

  outputs = inputs@{ self, nixpkgs, flake-parts, theme }:
    inputs.flake-parts.lib.mkFlake { inherit inputs; } {
      systems = [
        "x86_64-linux"
        "x86_64-darwin"
        "aarch64-darwin"
      ];

      perSystem = { pkgs, ... }:
        let
          themeName = ((builtins.fromTOML (builtins.readFile "${theme}/theme.toml")).name);
        in
        {

          packages.default = pkgs.stdenv.mkDerivation rec {
            pname = "jesusmtnez-website";
            version = (builtins.substring 0 8 self.lastModifiedDate);
            src = ./.;
            nativeBuildInputs = [ pkgs.hugo ];
            configurePhase = ''
              mkdir -p "themes/${themeName}"
              cp -r ${theme}/* "themes/${themeName}"
            '';
            buildPhase = "hugo --destination $out";
            dontInstal = true;
          };

          devShells.default = pkgs.mkShell {
            name = "website-shell";
            packages = [ pkgs.hugo ];
            shellHook = ''
              mkdir -p themes
              [[ ! -d themes/${themeName} ]] && ln -sn ${theme} themes/${themeName}
            '';
          };
        };
    };
}
