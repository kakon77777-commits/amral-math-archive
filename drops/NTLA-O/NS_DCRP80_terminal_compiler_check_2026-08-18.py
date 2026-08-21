# DCRP80 terminal-compiler audit
mapping = {'D79_alignment_boundary_rho_to_zero': ['X', 'R_state'], 'D79_tilt_blowup_rho_to_infinity': ['R_fil', 'R_state'], 'D79_strain_shape_blowup': ['R_state'], 'D79_support_or_ancestry_escape': ['R_tail'], 'D79_filamentation_or_director_oscillation': ['R_fil'], 'D79_packet_multiplicity_explosion': ['R_state'], 'D79_singular_material_injection': ['R_state'], 'prelimit_second_order_viscous_Kelvin_residue': ['R_K']}
terminal = {"X", "R_tail", "R_fil", "R_state", "R_K"}

used = set()
for src, dsts in mapping.items():
    if not dsts:
        raise AssertionError(f"Unmapped D79 mode: {src}")
    bad = set(dsts) - terminal
    if bad:
        raise AssertionError(f"New terminal coordinate accidentally introduced by {src}: {bad}")
    used.update(dsts)

print("D79 modes audited:", len(mapping))
print("Terminal coordinates used:", sorted(used))
print("No fifth terminal coordinate:", used <= terminal)

print("\nAbsorption map:")
for src, dsts in mapping.items():
    print(f"- {src} -> {' OR '.join(dsts)}")

print(
    "\nFinal compiler: O_PFET AND "
    "(X OR R_tail OR R_fil OR R_state OR R_K)"
)
